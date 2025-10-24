from bluemath_tk.wrappers.swash.swash_wrapper import SwashModelWrapper
import numpy as np
import os.path as op

class SwashModelWrapper_ondas(SwashModelWrapper):
    """
    Wrapper for the SWASH model with vegetation.
    """

    def build_case(self, case_context: dict, case_dir: str) -> None:
        super().build_case(case_context=case_context, case_dir=case_dir)

        # Save depth.bot
        np.savetxt(op.join(case_dir, "depth.bot"), self.depth_array)
 
class SwashModelWrapper_shoaling(SwashModelWrapper):
    """
    Wrapper for the SWASH model with vegetation.
    """

    def build_case(self, case_context: dict, case_dir: str) -> None:
        super().build_case(case_context=case_context, case_dir=case_dir)

        # Save depth.bot
        np.savetxt(op.join(case_dir, "depth.bot"), self.depth_array)