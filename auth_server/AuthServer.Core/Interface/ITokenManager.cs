using AuthServer.Database.Entity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Core.Interface
{
    public interface ITokenManager
    {
        public string GenerateToken(User user);
        public  string VerifyToken(string token);
    }
}
