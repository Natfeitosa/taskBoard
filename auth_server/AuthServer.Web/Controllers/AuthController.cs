﻿using AuthServer.Core.Interface;
using AuthServer.Core.Model;
using AuthServer.Web.Dto;
using Microsoft.AspNetCore.Authorization;
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
      var logInData = new LoginData() { Password = data.Password, Username = data.Username };
      var token = await _userManager.LogInUser(logInData);
      var tokenDto = new UserTokenDto() { AccessToken = token.AccessToken, RefreshToken = token.RefreshToken };
      return Ok(tokenDto);
    }

    [HttpPost("/register")]
    public async Task<ActionResult> RegisterUser(RegisterUserDto data)
    {
      var registerUser = new RegisterUser()
      {
        Email = data.Email,
        Password = data.Password,
        FirstName = data.FirstName,
        LastName = data.LastName,
      };
      await _userManager.RegisterUser(registerUser);
      return Ok();
    }

    [Authorize]
    [HttpGet("/verify")]
    public ActionResult HealthCheck()
    {
      return Ok();
    }


  }
}
