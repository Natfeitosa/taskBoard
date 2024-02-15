namespace AuthServer.Web.Dto
{
    public class UserToken
    {
        public required string AccessToken { get; set; }
        public required string RefreshToken { get; set; }
    }
}
