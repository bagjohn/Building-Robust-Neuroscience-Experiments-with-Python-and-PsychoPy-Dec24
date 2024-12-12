from experiment import main
from unittest.mock import Mock, patch

with patch("experiment.core.wait", return_value="hi"), patch("experiment.core.quit", side_effect=my_mock):
    main()