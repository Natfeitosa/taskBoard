using AuthServer.Core.Interface;
using AuthServer.Web.Dto;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Core.Manager
{
    public class UserManager : IUserManager
    {
        public Task<UserToken> LogInUser(LogInDto data)
        {
            throw new NotImplementedException();
        }

        public Task RegisterUser(RegisterUserDto data)
        {
            throw new NotImplementedException();
        }
    }
}
