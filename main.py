# This entrypoint file to be used in development. Start by reading README.md
import medical
from unittest import main

# Test your function by calling it here
medical.draw_cat_plot()
medical.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)
