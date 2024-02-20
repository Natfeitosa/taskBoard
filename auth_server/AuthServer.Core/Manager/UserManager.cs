using AuthServer.Core.Interface;
using AuthServer.Core.Model;
using AuthServer.Database.Entity;
using AuthServer.Database.Interface;


namespace AuthServer.Core.Manager
{
    public class UserManager : IUserManager
    {
        private readonly IUserRepository _userRepository;
        public UserManager(IUserRepository userRepo) {
        _userRepository = userRepo;
        }
        public async Task<UserToken> LogInUser(LoginData data)
        {
            var user = await _userRepository.GetUserByEmailAsync(data.Username);
            //TODO: ADD LOGIC OR GLOBAL HANDLER FOR FAILED LOG IN
            if(user == null || data.Password != data.Password) { throw new Exception("Failed to log in"); }
            //TODO: ADD LOGIC TO GENERATE JWT AND SAVE IT IN ORDER TO REFRESH IT
            var token = new UserToken() { AccessToken = "access Token", RefreshToken = "Refresh Token" };
            return token;
        }

        public async Task RegisterUser(User data)
        {
            var user = await _userRepository.GetUserByEmailAsync(data.Email);
            if(user != null) { throw new Exception("User account alreadty exist"); }
            await _userRepository.InsertAsync(data);

        }
    }
}
