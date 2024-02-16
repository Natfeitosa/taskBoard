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
        public Task<User> GetUserByEmailAsync(string email);
    }
}
