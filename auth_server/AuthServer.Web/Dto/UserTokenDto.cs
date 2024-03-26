namespace AuthServer.Web.Dto
{
    public class UserTokenDto
    {
        public required string AccessToken { get; set; }
        public required string RefreshToken { get; set; }
    }
}
