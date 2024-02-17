using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Entity
{
    public class User:BaseEntity
    {
        public required string Name { get; set;}
        [Required]
        public required string Email { get; set;}
        public required string Password { get; set;}

    }
}
