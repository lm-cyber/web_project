import os


# DB_HOST = os.environ.get("DB_HOST")
# DB_PORT = os.environ.get("DB_PORT")
# DB_NAME = os.environ.get("DB_NAME")
# DB_USER = os.environ.get("DB_USER")
# DB_PASS = os.environ.get("DB_PASS")
# SECRET = os.environ.get("SECRET")
# PASS_HASH_SUPERUSER = os.environ.get("PASS_HASH_SUPERUSER")

#
SECRET = """
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBALjl35bCKlBwEyDR
oCSDAbynqRmW0AJRLOgE+aR/gabnXA76jIW7Vn/53a7sQ/e/S1vS1hds0l5NI78T
uqSbftjYau//IhfZsd40ROOKwm9nNXwo0yuWD2m/xRdquaQDhlT3AIGTNS+mTAvC
KxbdYwyqfk4ILY9JkgjnJezfNIK3AgMBAAECgYEAtfPZFPXcSC4SVNCVRHj7g5iG
ax0jc7RIecczmDK19vZkfIUJNi1GEUhlZFczB6HjWehgMMsxNgW5cLbMjGJM7xCV
QPtSvo5XkRGPqAEzC4SdVYP7YBRfsOqmoGE3V1jzzGBrpkor5eu/GemEftYF8ugw
eX9r38B1m2xpizEUOPkCQQDqpH6QSK8cjFLRH7DKvboaeqgJ/S67/UeY28zEEgXZ
SJX7Q2yhCfQwPqlBHHEsF3VDT7LfCrhsYhbqen85/Z4NAkEAybpCOfEgfbT0Qkma
geSLivFyhN7OuWM0KPAA95u4H7WxV/K812Pxa8BlLE/4exLlfCq4pV6fQk6R4BHw
soa20wJAPnKdBIVzpWNrPyDyCmNIPnfadR4e7AVSosoMyzoIuHVrBT5CkPF3PcfP
f/az4Ao2OT3i2x2dS6snciw75BEtmQJABJSGDGq9Ih2JrjedmnVl9bGlt/6XEv59
oLBSVUzj0VR+wlBwmTNbt+aWZXsrWSAEtd0CdD7Bvu+pwDyoCmWkoQJBAMk0VMPS
vxu4PYwHiNVTkIL73MJFIZy2K5gjXu55WTa00EHzFMmuuhurYYiyFiR3shIJYpRX
uzfbPUkAUaseWB0=
"""
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "docker"
DB_USER = "docker"
DB_PASS = "docker"
PASS_HASH_SUPERUSER = "scrypt:32768:8:1$dpr1392m2tJy8Y1J$2c6d78e7e42233922cf5c99005fc4d23a6d472c05f07c8a3fc56b4473bc10ff66e588d189dc05e87355fd5afc369e5f04b72b443ca7553f66db4ec24c56b13b0"
