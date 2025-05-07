from typing import Dict, List

class TreasuryEngine:
    """
    Aligns Builder Core’s resourcing with system priorities and values.
    Supports funding allocation, wallet creation, tokenomics, and founder stewardship.
    """
    def __init__(self):
        self.priorities: List[str] = []
        self.wallets: Dict[str, str] = {}
        self.tokens: Dict[str, Dict] = {}

    def set_priority(self, focus: str):
        self.priorities.append(focus)

    def create_wallet(self, name: str, address: str):
        self.wallets[name] = address

    def define_tokenomics(self, module: str, supply: int, utility: str, rules: str):
        self.tokens[module] = {
            "supply": supply,
            "utility": utility,
            "rules": rules
        }

    def get_token_model(self, module: str) -> Dict:
        return self.tokens.get(module, {})

    def prioritize_founder_support(self):
        self.set_priority("Ensure ample, stress-free resourcing for James Sunheart and Sunheart Treasury & Trust")