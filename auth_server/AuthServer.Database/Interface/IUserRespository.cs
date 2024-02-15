using AuthServer.Database.Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Interface
{
    public interface IUserRespository:IRepository
    {
        public Task<User> GetUserById(Guid id);
        public Task<ICollection<User>> GetAllUsers();
        public Task DeleteUserById(User user);
    }
}
