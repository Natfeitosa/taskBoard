using AuthServer.Core.Exceptions;

namespace AuthServer.Web.ExceptionHandlers
{
    public static class Constants
    {
        public static Dictionary<Type, int> ExceptionDictionary { get; } = new Dictionary<Type, int>() {
            {typeof(FailLogInException), 401 },
            {typeof(InvalidEmailException),400 },
            {typeof(UserAlreadyExistException),400 }
        };
    }
}
