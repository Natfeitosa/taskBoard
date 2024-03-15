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

        /// <summary>
        /// Updates Entity in the Database
        /// </summary>
        /// <param name="entity">Entity to Update</param>
        public Task UpdateAsync(T entity);

        /// <summary>
        /// Deletes given Entity from Database
        /// </summary>
        /// <param name="entity">Entity to Delete</param>
        public Task DeleteAsync(T entity);

        /// <summary>
        /// Get Entity By Id
        /// </summary>
        /// <param name="id">Id of the User</param>
        /// <returns>Returns Null if Entity does not exist</returns>
        public Task<T?> GetById(Guid id);

        /// <summary>
        /// Gets a List of all users
        /// </summary>
        /// <returns></returns>
        public Task<ICollection<T>> GetAll();

    }
}
