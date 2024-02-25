using AuthServer.Core.Interface;
using AuthServer.Core.Model;
using AuthServer.Database.Entity;
using AuthServer.Database.Interface;


namespace AuthServer.Core.Manager
{
    public class UserManager : IUserManager
    {
        private readonly IUserRepository _userRepository;
        private readonly ITokenManager _tokenManager;
        public UserManager(IUserRepository userRepo, ITokenManager tokenManager) {
        _userRepository = userRepo;
            _tokenManager = tokenManager;
        }
        public async Task<UserToken> LogInUser(LoginData data)
        {
            var user = await _userRepository.GetUserByEmailAsync(data.Username);
            //TODO: ADD LOGIC OR GLOBAL HANDLER FOR FAILED LOG IN
            if(user == null || data.Password != data.Password) { throw new Exception("Failed to log in"); }
            var accessToken = _tokenManager.GenerateToken(user);
            return new UserToken() { AccessToken = accessToken, RefreshToken = accessToken };
        }

        public async Task RegisterUser(RegisterUser data)
        {
            
            var user = await _userRepository.GetUserByEmailAsync(data.Email);
            //TODO:Add logic to handle when user already exist
            if(user != null) { throw new Exception("User account alreadty exist"); }
            var id = Guid.NewGuid();

            var newUser = new User() {
            IsDeleted = false,
            Id = id,
            FirstName = data.FirstName,
            LastName = data.LastName,
            Email = data.Email,
            Password = data.Password,
            };
            await _userRepository.InsertAsync(newUser);

        }

       
    }
}
