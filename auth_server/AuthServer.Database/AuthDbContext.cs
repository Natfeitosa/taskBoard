using AuthServer.Database.Entity;
using Microsoft.EntityFrameworkCore;


namespace AuthServer.Database
{
    public class AuthDbContext:DbContext
    {
        public AuthDbContext(DbContextOptions<AuthDbContext> options) : base(options) { }
        public DbSet<User> Users { get; set; }
    }
}
