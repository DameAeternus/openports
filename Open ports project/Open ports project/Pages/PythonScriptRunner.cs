using System.Diagnostics;

public static class PythonScriptRunner
{
    public static string RunScript(string scriptPath, string arguments)
    {
        var processInfo = new ProcessStartInfo
        {
            FileName = "python",
            Arguments = $"{scriptPath} {arguments}",
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using (var process = new Process())
        {
            process.StartInfo = processInfo;
            process.Start();

            // Read the output of the Python script
            string result = process.StandardOutput.ReadToEnd();

            return result;
        }
    }
}
