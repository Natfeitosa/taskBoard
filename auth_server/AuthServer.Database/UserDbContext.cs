using AuthServer.Database.Entity;
using Microsoft.EntityFrameworkCore;

namespace AuthServer.Database
{
    public class UserDbContext:DbContext
    {
        public DbSet<User> Users { get; set; }

        public UserDbContext(DbContextOptions<UserDbContext> options):base(options) { }
    } 
}