export PANTS_CONFIG_FILES=pants.ci.toml

# Then, your normal CI setup
./pants setup-py --args="bdist_wheel" ::
