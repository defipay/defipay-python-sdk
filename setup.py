from setuptools import setup
setup(
    name="defipay",
    version="0.30",
    author="Defipay",
    author_email="support@defipay.biz",
    description="Defipay restful api",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Defipay Copyright Reserved",
    python_requires=">=3.7",
    url="https://github.com/defipay/defipay-python-api",
    packages=['defipay', 'defipay.signer', 'defipay.client', 'defipay.error', 'defipay.config'],
    include_package_data=True,
    install_requires=["ecdsa==0.17.0", "requests"]
    # zip_safe=False,
)
