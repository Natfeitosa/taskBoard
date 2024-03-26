using AuthServer.Core.Exceptions;
using AuthServer.Core.Interface;
using AuthServer.Core.Model;
using AuthServer.Database.Entity;
using AuthServer.Database.Interface;
using Org.BouncyCastle.Crypto.Prng;
using System.Net;
using System.Web.Helpers;
using System.Web.Http;


namespace AuthServer.Core.Manager
{
    public class UserManager : IUserManager
    {
        private readonly IUserRepository _userRepository;
        private readonly ITokenManager _tokenManager;
        public UserManager(IUserRepository userRepo, ITokenManager tokenManager)
        {
            _userRepository = userRepo;
            _tokenManager = tokenManager;
        }

        public async Task DeleteAllUsers()
        {
            await _userRepository.DeleteAllUsers();
        }

        public async Task<UserToken> LogInUser(LoginData data)
        {
            if (!data.Username.Contains('@') && !data.Username.Contains('.'))
            {
                throw new InvalidEmailException("Invalid Email");
            }
            var user = await _userRepository.GetUserByEmailAsync(data.Username);
            //TODO: ADD LOGIC OR GLOBAL HANDLER FOR FAILED LOG IN
            if (user == null || !CheckPassword(data.Password,user.Password)) { throw new FailLogInException("Fail To log in"); }
            var accessToken = _tokenManager.GenerateToken(user);
            return new UserToken() { AccessToken = accessToken, RefreshToken = accessToken };
        }
        private bool CheckPassword(string password, string savedPassword)
        {
           return Crypto.VerifyHashedPassword(savedPassword,password);

        }
        public async Task RegisterUser(RegisterUser data)
        {

            var user = await _userRepository.GetUserByEmailAsync(data.Email);
            //TODO:Add logic to handle when user already exist
            if (user != null) { throw new UserAlreadyExistException("User account alreadty exist"); }
            var id = Guid.NewGuid();
            var password = Crypto.HashPassword(data.Password);
            var newUser = new User()
            {
                IsDeleted = false,
                Id = id,
                FirstName = data.FirstName,
                LastName = data.LastName,
                Email = data.Email,
                Password = password,
            };
            await _userRepository.InsertAsync(newUser);

        }

       


    }
}
