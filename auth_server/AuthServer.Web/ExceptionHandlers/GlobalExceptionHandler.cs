using Microsoft.AspNetCore.Diagnostics;
using Microsoft.AspNetCore.Mvc;

namespace AuthServer.Web.ExceptionHandlers
{
    internal sealed class GlobalExceptionHandler : IExceptionHandler

    {
        private readonly ILogger _logger;
        public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger)
        {
            _logger = logger;
        }
        public async ValueTask<bool> TryHandleAsync(HttpContext httpContext, Exception exception, CancellationToken cancellationToken)
        {
            _logger.LogError(exception, $"Exception occured: {exception.Message}");
            var problemDetails = new ProblemDetails {
                Status = GetStatusCode(exception),
                Title = "Error Processing Request"
            };
            httpContext.Response.StatusCode = problemDetails.Status.Value;
            await httpContext.Response.WriteAsJsonAsync( problemDetails, cancellationToken );
            return true;
        }
        private int GetStatusCode<T>(T exception)
        {
            if (Constants.ExceptionDictionary.ContainsKey(exception.GetType()))
            {
                return Constants.ExceptionDictionary[exception.GetType()];
            }
            else
            {
                return 500;
            }
        }
    }
}
