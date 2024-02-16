using AuthServer.Database.Entity;
using AuthServer.Database.Interface;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Repository
{
    public class UserRepository:IUserRepository
    {
        private AuthDbContext _authDbContext;
        private DbSet<User> UserSet;
        public UserRepository(AuthDbContext context)
        {
            _authDbContext = context;
            UserSet = context.Users;
        }

        public Task DeleteAsync(User entity)
        {
            throw new NotImplementedException();
        }

        public Task<ICollection<User>> GetAll()
        {
            throw new NotImplementedException();
        }

        public Task<User> GetById(Guid id)
        {
            throw new NotImplementedException();
        }

        public Task<User> GetUserByEmailAsync(string email)
        {
            throw new NotImplementedException();
        }

        public async Task InsertAsync(User entity)
        {
            await UserSet.AddAsync(entity);
            await SaveContext();
        }

        public async Task UpdateAsync(User entity)
        {
            UserSet.Update(entity);
            await SaveContext();
            
        }
        private async Task SaveContext()
        {
           await _authDbContext.SaveChangesAsync();
        }
    }
}
