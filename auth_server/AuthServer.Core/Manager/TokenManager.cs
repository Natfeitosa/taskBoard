using AuthServer.Core.Interface;
using AuthServer.Core.Options;
using AuthServer.Database.Entity;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Collections.Generic;
using System.IdentityModel.Tokens.Jwt;
using System.Linq;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Core.Manager
{
    public class TokenManager : ITokenManager
    {
        private readonly JwtOptions jwtOptions;
        public TokenManager(IOptions<JwtOptions> options) {
        jwtOptions = options.Value;
        }
        public string GenerateToken(User user)
        {
            var securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtOptions.Key));
            var credentials = new SigningCredentials(securityKey,SecurityAlgorithms.HmacSha256);
            var claims = new[]
            {
                new Claim(ClaimTypes.NameIdentifier,user.Email),
                new Claim(ClaimTypes.GivenName, user.LastName),
                new Claim(ClaimTypes.Name, user.FirstName),
            };
            var token = new JwtSecurityToken(
                jwtOptions.Issuer,jwtOptions.Audience,
                claims,
                expires:DateTime.Now.AddMinutes(30),
                signingCredentials:credentials);

            return new JwtSecurityTokenHandler().WriteToken(token);
         }

        public string VerifyToken(string token)
        {
            //To verify the token we can check the Claims to see who the user is. Try to check who signed the token to see if the token has been modified
            //The signing credentials are already part of the token validation
            throw new NotImplementedException();
        }
    }
}
