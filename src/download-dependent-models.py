import os

list_of_ietf_models =\
[ ["ietf-bgp", "draft-ietf-idr-bgp-model", "16"],
  ["ietf-tcp", "draft-ietf-tcpm-yang-tcp", "09"],
  ["ietf-tcp-common", "draft-ietf-netconf-tcp-client-server", "15"],
  ["ietf-srv6-types", "draft-ietf-spring-srv6-yang", "02"],
  ["ietf-srv6-base", "draft-ietf-spring-srv6-yang", "02"],
  ["iana-bgp-types", "draft-ietf-idr-bgp-model", "16"],
  ["iana-bgp-community", "draft-ietf-idr-bgp-model", "16"],
  ["ietf-bgp-common", "draft-ietf-idr-bgp-model", "16"],
  ["iana-bgp-notification", "draft-ietf-idr-bgp-model", "16"],
  ["ietf-bgp-policy", "draft-ietf-idr-bgp-model", "16"] ]


def fetch_and_extract(draft, module, version):
    print("Fetching file " + draft + " with version " + version)
    draft_version = draft + "-" + version
    print(draft_version)
    os.system('curl -sO https://www.ietf.org/archive/id/%s.txt' %draft_version)
    print("Extracting Module from " + draft_version)
    os.system('xym %s.txt' %draft_version)
    print("Moving module " + module + " to ../bin/imported-modules/")
    os.system('mv %s* ../bin/imported-modules/' %module)
    print("Cleaning up ...")
    os.system('rm %s.txt' %draft_version)

def fetch(module, path):
    file = path + module + ".yang.txt"
    print("Fetching file " + file)
    os.system('curl -sO http://%s' %file)
    model = module + ".yang"
    print("Moving module " + model + " to ../bin/imported-modules/")
    os.system("mv '%s'.txt ../bin/imported-modules/'%s'" %(model, model))

os.system("mkdir -p ../bin/imported-modules")

for list in list_of_ietf_models:
    module, draft, version = list
    print(module)
    fetch_and_extract(draft, module, version)

os.system('rm *.yang')
