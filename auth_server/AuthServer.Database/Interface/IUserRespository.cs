using AuthServer.Database.Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Interface
{
    public interface IUserRepository:IRepository<User>
    {
        /// <summary>
        /// Gets a User by Email
        /// </summary>
        /// <param name="email">Email of the User</param>
        /// <returns>User If found, otherwise null</returns>
        public Task<User?> GetUserByEmailAsync(string email);
    }
}
