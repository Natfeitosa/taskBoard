using System;
namespace AuthServer.Core.Exceptions
{
    public class FailLogInException : Exception
    {
        public FailLogInException() { }
        public FailLogInException(string message) : base(message) { }
        public FailLogInException(string message, Exception inner) : base(message, inner) { }

    }
}
