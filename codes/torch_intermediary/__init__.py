"""
from bitsandbytes.nn import Linear8bitLt as Linear
from bitsandbytes.nn import StableEmbedding as Embedding
from bitsandbytes.optim.adam import Adam8bit as Adam
from bitsandbytes.optim.adamw import AdamW8bit as AdamW
"""
"""
from torch.nn import Linear
from torch.nn import Embedding
from torch.optim.adam import Adam
from torch.optim.adamw import AdamW
"""

OVERRIDE_LINEAR = False
OVERRIDE_EMBEDDING = False
OVERRIDE_ADAM = True
OVERRIDE_ADAMW = True
USE_STABLE_EMBEDDING = True

if OVERRIDE_LINEAR:
	from bitsandbytes.nn import Linear8bitLt as Linear
else:
	from torch.nn import Linear

if OVERRIDE_EMBEDDING:
	if USE_STABLE_EMBEDDING:
		from bitsandbytes.nn import StableEmbedding as Embedding
	else:
		from bitsandbytes.nn import Embedding as Embedding
else:
	from torch.nn import Embedding

if OVERRIDE_ADAM:
	from bitsandbytes.optim.adam import Adam8bit as Adam
else:
	from torch.optim.adam import Adam

if OVERRIDE_ADAMW:
	from bitsandbytes.optim.adamw import AdamW8bit as AdamW
else:
	from torch.optim.adamw import AdamW