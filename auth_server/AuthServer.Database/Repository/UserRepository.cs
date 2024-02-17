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

        public async Task DeleteAsync(User entity)
        {
            UserSet.Remove(entity);
            await SaveContext();
        }

        public async Task<ICollection<User>> GetAll()
        {
            var users = await UserSet.ToListAsync();
            return users;
        }

        public async Task<User?> GetById(Guid id)
        {
            var user = await UserSet.SingleOrDefaultAsync(x => x.Id == id);
            return user;
        }

        public async Task<User?> GetUserByEmailAsync(string email)
        {
            var user = await UserSet.SingleOrDefaultAsync(x => x.Email == email);
            return user;
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
