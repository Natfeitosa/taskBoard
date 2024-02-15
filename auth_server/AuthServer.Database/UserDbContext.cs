using AuthServer.Database.Entity;
using Microsoft.EntityFrameworkCore;

namespace AuthServer.Database
{
    public class UserDbContext:DbContext
    {
        public DbSet<User> Users { get; set; }
    }
}