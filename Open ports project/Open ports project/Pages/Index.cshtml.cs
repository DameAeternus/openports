using Microsoft.AspNetCore.Mvc;
using Open_ports_project;  // Add the appropriate namespace

public class HomeController : Controller
{
    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public IActionResult Scan(string ip, string ports)
    {
        // Call the Python script using the PythonScriptRunner
        string result = PythonScriptRunner.RunScript("E:\\Desktop\\python project\\scan.py", $"{ip} {ports}");

        ViewData["Result"] = result;

        return View("ScanResult");
    }
}

