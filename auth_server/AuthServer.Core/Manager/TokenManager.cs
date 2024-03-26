using AuthServer.Core.Interface;
using AuthServer.Core.Options;
using AuthServer.Database.Entity;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace AuthServer.Core.Manager
{
  public class TokenManager : ITokenManager
  {
    private readonly JwtOptions jwtOptions;
    public TokenManager(IOptions<JwtOptions> options)
    {
      jwtOptions = options.Value;
    }
    public string GenerateToken(User user)
    {
      var securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtOptions.Key));
      var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);
      var claims = new[]
      {
                new Claim(ClaimTypes.NameIdentifier,user.Email),
                new Claim(ClaimTypes.GivenName, user.LastName),
                new Claim(ClaimTypes.Name, user.FirstName),
            };
      var token = new JwtSecurityToken(
          jwtOptions.Issuer, jwtOptions.Audience,
          claims,
          expires: DateTime.Now.AddMinutes(30),
          signingCredentials: credentials);

      return new JwtSecurityTokenHandler().WriteToken(token);
    }

  }
}
