using AuthServer.Core.Interface;
using AuthServer.Core.Model;
using AuthServer.Web.Dto;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AuthServer.Web.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AuthController : ControllerBase
    {
        private IUserManager _userManager;
        public AuthController(IUserManager userManager)
        {
            _userManager = userManager;
        }
        [HttpPost("/logIn")]
        public async Task<ActionResult<UserTokenDto>> LogInUser(LogInDto data)
        {
            var logInData = new LoginData() { Password = data.Password, Username= data.Username };
            _userManager.LogInUser(logInData);
            return Ok();
        }

        [HttpPost("/register")]
        public async Task<ActionResult> RegisterUser(RegisterUserDto data)
        {
            return Ok();
        }
    }
}
