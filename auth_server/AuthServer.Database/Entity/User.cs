using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Entity
{
    public class User
    {
        public int Id { get; set;}
        public required string Name { get; set;}
        public required string Email { get; set;}
        public required string Password { get; set;}

    }
}
