using AuthServer.Web.Dto;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace AuthServer.Web.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AuthController : ControllerBase
    {
        [HttpPost("/logIn")]
        public async Task<ActionResult<UserToken>> LogInUser(LogInDto data)
        {
            return Ok();
        }
    }
}
