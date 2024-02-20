using AuthServer.Core.Interface;
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
            return Ok();
        }

        [HttpPost("/register")]
        public async Task<ActionResult> RegisterUser(RegisterUserDto data)
        {
            return Ok();
        }
    }
}
