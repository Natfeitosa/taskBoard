using AuthServer.Web.Dto;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Core.Interface
{
    public interface IUserManager
    {
        Task<UserToken> LogInUser(LogInDto data);
        Task RegisterUser(RegisterUserDto data);
    }
}
