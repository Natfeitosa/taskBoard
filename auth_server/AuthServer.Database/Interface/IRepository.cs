using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Interface
{
    public interface IRepository
    {
        /// <summary>
        /// Inserts Entity to database
        /// </summary>
        /// <returns></returns>
        public Task InsertAsync();
        public Task UpdateAsync();
        public Task DeleteAsync();
        public Task GetById();
        public Task<ICollection> GetAll();
    }
}
