using AuthServer.Core.Manager;
using AuthServer.Core.Options;
using AuthServer.Database.Entity;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Logging;
using Microsoft.IdentityModel.Tokens;
using Moq;
using Org.BouncyCastle.Bcpg.OpenPgp;
using System.IdentityModel.Tokens.Jwt;
using System.Text;
using ZstdSharp.Unsafe;


namespace AuthServer.Test.ManagersTest
{
    public class TokenManagerTest
    {
        [Fact]
        public void Should_Generate_Token()
        {
            var mockOptions = new Mock<IOptions<JwtOptions>>();
            const string testAudience = "TEST";
            const string testIssuer = "TESTISSUER";
            const string testKey = "7acb654c-7017-4c0f-8b9a-68128aae7c13";
            
            var testId = Guid.NewGuid();
            var testName = "testName";
            var testEmail = "TestEmail";
            var testLastName = "TestLastName";
            var testPassword = "TestPassword";
            
            mockOptions.Setup(options => options.Value).Returns(new JwtOptions() { Audience=testAudience,Issuer = testIssuer,Key=testKey});
            
            var tokenManager = new TokenManager(mockOptions.Object);
            var testUser = new User()
            {
                Id = testId,
                FirstName = testName,
                LastName = testLastName,
                Email = testEmail,
                IsDeleted = false,
                Password = testPassword
            };
            SecurityToken validateToken;
            var token =  tokenManager.GenerateToken(testUser);
            var tokenValidation = GetTokenValidationParameters(testIssuer,testAudience,testKey);
           var principle = new JwtSecurityTokenHandler().ValidateToken(token,tokenValidation,out validateToken);

            Assert.NotNull(token);
            //if it fails to validation the princilple will be null
            Assert.NotNull(principle);
            
        }

        [Fact]
        public void Token_should_fail_to_validate()
        {
            var mockOptions = new Mock<IOptions<JwtOptions>>();
            const string testAudience = "TEST";
            const string testIssuer = "TESTISSUER";
            const string realKey = "7acb654c-7017-4c0f-8b9a-68128aae7c13";
            const string fakeKey = "766bc9bf-af2a-41fd-9007-ce9e6a0f3c91";
            var testId = Guid.NewGuid();
            var testName = "testName";
            var testEmail = "TestEmail";
            var testLastName = "TestLastName";
            var testPassword = "TestPassword";

            mockOptions.Setup(options => options.Value).Returns(new JwtOptions() { Audience = testAudience, Issuer = testIssuer, Key = realKey });
            
            var tokenManager = new TokenManager(mockOptions.Object);
            var testUser = new User()
            {
                Id = testId,
                FirstName = testName,
                LastName = testLastName,
                Email = testEmail,
                IsDeleted = false,
                Password = testPassword
            };
            SecurityToken validateToken;
            var token = tokenManager.GenerateToken(testUser);
            var tokenValidation = GetTokenValidationParameters(testIssuer, testAudience, fakeKey);
            Assert.Throws<SecurityTokenSignatureKeyNotFoundException>(() =>
            {
                var principle = new JwtSecurityTokenHandler().ValidateToken(token, tokenValidation, out validateToken);
            });
                
          
         
        }
        private TokenValidationParameters GetTokenValidationParameters(string issuer, string audience,string key)
        {
            IdentityModelEventSource.ShowPII = true;
            var tokenValidation = new TokenValidationParameters();
            tokenValidation.ValidIssuer = issuer;
            tokenValidation.ValidAudience = audience;
            tokenValidation.IssuerSigningKey = new Microsoft.IdentityModel.Tokens.SymmetricSecurityKey(Encoding.UTF8.GetBytes(key));
            return tokenValidation;
        }
    }
}
