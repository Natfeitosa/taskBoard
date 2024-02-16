using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AuthServer.Database.Interface
{
    public interface IRepository<T>
    {
        /// <summary>
        /// Inserts Entity to database
        /// </summary>
        /// <returns></returns>
        public Task InsertAsync(T entity);
        public Task UpdateAsync(T entity);
        public Task DeleteAsync(T entity);
        public Task<T> GetById(Guid id);
        public Task<ICollection<T>> GetAll();
    }
}
