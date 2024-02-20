using AuthServer.Core.Interface;
using AuthServer.Core.Manager;
using AuthServer.Database;
using AuthServer.Database.Interface;
using AuthServer.Database.Repository;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddTransient<IUserManager,UserManager>();
builder.Services.AddTransient<IUserRepository, UserRepository>();
var connectionString = builder.Configuration.GetConnectionString("MySqlString");


builder.Services.AddDbContext<AuthDbContext>(options =>
{
    options.UseMySQL(connectionString);
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
