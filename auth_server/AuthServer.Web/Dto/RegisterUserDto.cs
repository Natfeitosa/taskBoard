namespace AuthServer.Web.Dto
{
    public class RegisterUserDto
    {
        
        public required string FirstName { get; set; }
        public required string LastName { get; set;}
        public required string Email { get; set;}
        public required string Password { get; set;}
        
    }
}
