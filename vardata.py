avlist = [
    "Can the attacker utilize some type of network or communication protocol to exploit this vulnerability?", 
    "Does the network use OSI layer 3 or 4 protocols, e.g. IP, TCP/IP, or UDP?",
    "Must the attacker have physical contact with the device?",
    "AV = Network (N)",
    "Is the communication over a wireless channel? ",
    "Can the attacker utilize some type of network or communication protocol to exploit this vulnerability? -- Yes",
    "Can the attacker utilize some type of network or communication protocol to exploit this vulnerability? -- No",
    "Can the attacker utilize some type of network or communication protocol to exploit this vulnerability? -- Unkown",
    "Can the attacker utilize some type of network or communication protocol to exploit this vulnerability? -- Not answered",
    "Does the network use OSI layer 3 or 4 protocols, e.g. IP, TCP/IP, or UDP? -- Yes",
    "Does the network use OSI layer 3 or 4 protocols, e.g. IP, TCP/IP, or UDP? -- No",
    "Does the network use OSI layer 3 or 4 protocols, e.g. IP, TCP/IP, or UDP? -- Unkown",
    "Does the network use OSI layer 3 or 4 protocols, e.g. IP, TCP/IP, or UDP? -- Not answered",
    "Must the attacker have physical contact with the device? -- Yes ",
    "Must the attacker have physical contact with the device? -- No",
    "Must the attacker have physical contact with the device? -- Unkown",
    "Must the attacker have physical contact with the device? -- Not answered",
    "AV = Physical (P)",
    "AV = Local (L)",
    "Is the communication over a wireless channel? -- Yes ",
    "Is the communication over a wireless channel? -- No",
    "Is the communication over a wireless channel? -- Unkown",
    "Is the communication over a wireless channel? -- Not answered",
    "Is the range approximately 10 feet or less?",
    "AV = Adjacent (A)",
    "Is the range approximately 10 feet or less? -- Yes",
    "Is the range approximately 10 feet or less? -- No",
    "Is the range approximately 10 feet or less? -- Unkown",
    "Is the range approximately 10 feet or less? -- Not answered"
]

aclist = [
    "Can the attacker attempt to exploit the vulnerability at will, i.e., without requiring any special circumstances, configurations, or use of other vulnerabilities or attacks before attacking this vulnerability?",
    "AC = Low (L)",
    "AC = High (H)",
    "Can the attacker attempt to exploit the vulnerability at will, i.e., without requiring any special circumstances, configurations, or use of other vulnerabilities or attacks before attacking this vulnerability? -- Yes",
    "Can the attacker attempt to exploit the vulnerability at will, i.e., without requiring any special circumstances, configurations, or use of other vulnerabilities or attacks before attacking this vulnerability? -- No",
    "Can the attacker attempt to exploit the vulnerability at will, i.e., without requiring any special circumstances, configurations, or use of other vulnerabilities or attacks before attacking this vulnerability? -- Unkown"
]

prlist = [
    "Does the device/component use an authorization model that supports login for multiple different users or roles with different privilege levels? ",
    "Before attempting to exploit the vulnerability, must the attacker be authorized to the affected component?",
    "Must the attacker have administrator, maintainer, or other system-level privileges to attempt to exploit the vulnerability?",
    "PR = None (N)",
    "PR = Low (L)",
    "PR = High (H)",
    "Does the device/component use an authorization model that supports login for multiple different users or roles with different privilege levels? -- Yes",
    "Does the device/component use an authorization model that supports login for multiple different users or roles with different privilege levels? -- No ",
    "Does the device/component use an authorization model that supports login for multiple different users or roles with different privilege levels? -- Unkown",
    "Before attempting to exploit the vulnerability, must the attacker be authorized to the affected component? -- Yes",
    "Before attempting to exploit the vulnerability, must the attacker be authorized to the affected component? -- No",
    "Before attempting to exploit the vulnerability, must the attacker be authorized to the affected component? -- Unkown",
    "Must the attacker have administrator, maintainer, or other system-level privileges to attempt to exploit the vulnerability? -- Yes",
    "Must the attacker have administrator, maintainer, or other system-level privileges to attempt to exploit the vulnerability? -- No",
    "Must the attacker have administrator, maintainer, or other system-level privileges to attempt to exploit the vulnerability? -- Unkown",
]

uilist = [
    "To successfully exploit the vulnerability, must the attacker depend upon some user or victim to perform an action or otherwise interact with the system?",
    "UI = Required (R)",
    "UI = None (N)",
    "To successfully exploit the vulnerability, must the attacker depend upon some user or victim to perform an action or otherwise interact with the system? -- Yes",
    "To successfully exploit the vulnerability, must the attacker depend upon some user or victim to perform an action or otherwise interact with the system? -- No",
    "To successfully exploit the vulnerability, must the attacker depend upon some user or victim to perform an action or otherwise interact with the system? -- Unkown",
]

slist = [
    "Can the attacker affect a component whose authority (“authorization scope”) is different than that of the vulnerable component?",
    "S = Changed (C)",
    "S = Unchanged (U)",
    "Can the attacker affect a component whose authority (“authorization scope”) is different than that of the vulnerable component? -- Yes",
    "Can the attacker affect a component whose authority (“authorization scope”) is different than that of the vulnerable component? -- No",
    "Can the attacker affect a component whose authority (“authorization scope”) is different than that of the vulnerable component? -- Unkown",
]

clist = [
    "Is there any impact on confidentility?",
    "C = High (H)",
    "C = Low (L)",
    "C = None (N)",
    "Is there any impact on confidentility? -- Yes",
    "Is there any impact on confidentility? -- No",
    "Is there any impact on confidentility? -- Unkown",
    "Can the attacker obtain all information from the impacted component, or is the disclosed information critical?",
    "Can the attacker obtain all information from the impacted component, or is the disclosed information critical? -- Yes",
    "Can the attacker obtain all information from the impacted component, or is the disclosed information critical? -- No",
    "Can the attacker obtain all information from the impacted component, or is the disclosed information critical? -- Unkown",
]

ilist = [
    "Is there any impact on integrity?",
    "I = High (H)",
    "I = Low (L)",
    "I = None (N)",
    "Is there any impact on integrity? -- Yes",
    "Is there any impact on integrity? -- No",
    "Is there any impact on integrity? -- Unkown",
    "Can the attacker modify all information from the impacted component, or is the modifed nformation critical?",
    "Can the attacker modify all information from the impacted component, or is the modifyed information critical? -- Yes",
    "Can the attacker modify all information from the impacted component, or is the modifyed information critical? -- No",
    "Can the attacker modify all information from the impacted component, or is the modifyed information critical? -- Unkown",
]

alist = [
    "Is there any impact on availibility of a resource?",
    "A = High (H)",
    "A = Low (L)",
    "A = None (N)",
    "Is there any impact on availibility of a resource? -- Yes",
    "Is there any impact on availibility of a resource? -- No",
    "Is there any impact on availibility of a resource? -- Unkown",
    "Can the attacker completly deny access to the impacted component, or is the resource information critical?",
    "Can the attacker completly deny access to the impacted component, or is the resource information critical? -- Yes",
    "Can the attacker completly deny access to the impacted component, or is the resource information critical? -- No",
    "Can the attacker completly deny access to the impacted component, or is the resource information critical? -- Unkown",
]