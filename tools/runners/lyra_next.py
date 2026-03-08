#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 Hank Hsu.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from BaseRunner import BaseRunner


class lyra_next(BaseRunner):
    def __init__(self):
        super().__init__(
            "lyra-next", "lyra-next", supported_features={"parsing"})

        self.submodule = "third_party/tools/lyra-next"
        self.url = f"https://github.com/hankhsu1996/lyra-next/tree/{self.get_commit()}"

    def prepare_run_cb(self, tmp_dir, params):
        self.cmd = [self.executable, "check"]
        self.cmd += params['files']
