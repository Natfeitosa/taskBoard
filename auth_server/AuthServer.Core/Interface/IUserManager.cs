using AuthServer.Core.Model;
using AuthServer.Database.Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Core.Interface
{
    public interface IUserManager
    {
        /// <summary>
        /// Checks against the database to if the user account exist and correct Password was given. If the information is correct JWT will be sent back
        /// </summary>
        /// <param name="data">Log in data information</param>
        /// <returns>User JWT</returns>
        Task<UserToken> LogInUser(LoginData data);

        /// <summary>
        /// Registers a new user to the database
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        Task RegisterUser(RegisterUser data);

        Task DeleteAllUsers();
    }
}
