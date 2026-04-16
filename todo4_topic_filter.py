# ============================================================
# TODO 4: Implement topic_filter() - COMPLETED
#
# Check if user_input belongs to allowed topics.
# The VinBank agent should only answer about banking topics.
#
# Return True if input should be BLOCKED (off-topic or blocked topic).
# ============================================================

# Allowed topics for VinBank banking assistant
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    # Vietnamese (with and without diacritics)
    "tai khoan", "tài khoản", "tai kho", "tài kho",
    "giao dich", "giao dịch", "giao d",
    "tiet kiem", "tiết kiệm", "tiet k", "tiết k",
    "lai suat", "lãi suất", "lai su", "lãi su",
    "chuyen tien", "chuyển tiền", "chuyen t", "chuyển t",
    "the tin dung", "thẻ tín dụng", "the tin d",
    "so du", "số dư", "so d",
    "vay", "vay tiền", "vay ti",
    "ngan hang", "ngân hàng", "ngan h", "ngân h",
    "atm", "card", "debit",
    "mortgage", "investment", "finance", "money",
    "currency", "exchange", "rate", "fee",
]

# Blocked topics (if detected -> block immediately)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "porn", "sex", "adult",
    "bomb", "kill", "murder", "suicide", "death",
    "racist", "discrimination", "hate", "terrorism",
]

def topic_filter(user_input: str) -> bool:
    """Check if input is off-topic or contains blocked topics.
    
    Args:
        user_input: The user's message
    
    Returns:
        True if input should be BLOCKED (off-topic or blocked topic)
    """
    
    # Handle empty input
    if not user_input or len(user_input.strip()) == 0:
        return True  # Block empty messages
    
    input_lower = user_input.lower()
    
    # ============================================================
    # STEP 1: Check for BLOCKED topics (highest priority)
    # ============================================================
    for blocked_topic in BLOCKED_TOPICS:
        if blocked_topic in input_lower:
            return True  # BLOCK immediately
    
    # ============================================================
    # STEP 2: Check for ALLOWED topics
    # ============================================================
    # If input contains at least one allowed topic -> ALLOW
    for allowed_topic in ALLOWED_TOPICS:
        if allowed_topic in input_lower:
            return False  # ALLOW (on-topic)
    
    # ============================================================
    # STEP 3: If no allowed topic found -> BLOCK (off-topic)
    # ============================================================
    return True  # BLOCK (off-topic)


# ============================================================
# COMPREHENSIVE TEST SUITE
# ============================================================

def run_tests():
    """Run comprehensive tests on topic_filter()."""
    
    print("=" * 70)
    print("TODO 4: TOPIC FILTER - TEST RESULTS")
    print("=" * 70)
    
    test_cases = [
        # ===== ON-TOPIC (Should be False = ALLOW) =====
        ("What is the 12-month savings rate?", False),
        ("I want to transfer money to another account", False),
        ("How do I apply for a credit card?", False),
        ("What are the ATM withdrawal limits?", False),
        ("Can I check my account balance?", False),
        ("Lãi suất tiết kiệm là bao nhiêu?", False),  # Vietnamese
        ("Tôi muốn chuyển tiền", False),  # Vietnamese
        ("What is the interest rate for loans?", False),
        ("How to deposit money?", False),
        ("Tell me about mortgage options", False),
        
        # ===== OFF-TOPIC (Should be True = BLOCK) =====
        ("Recipe for chocolate cake", True),
        ("What is the weather today?", True),
        ("Who won the football match?", True),
        ("Tell me a joke", True),
        ("What is 2+2?", True),
        ("How to cook pasta?", True),
        ("Best movies of 2024", True),
        
        # ===== BLOCKED TOPICS (Should be True = BLOCK) =====
        ("How to hack a computer?", True),
        ("How to make a bomb?", True),
        ("Where to buy drugs?", True),
        ("Gambling tips", True),
        ("Violent content", True),
        ("Illegal activities", True),
        
        # ===== EDGE CASES =====
        ("", True),  # Empty input
        ("   ", True),  # Whitespace only
        ("a" * 1000, True),  # Very long off-topic
        ("I want to transfer money and also how to hack", True),  # Mixed (blocked wins)
        ("banking hack prevention tips", True),  # Contains both (blocked wins)
    ]
    
    passed = 0
    failed = 0
    
    for text, expected in test_cases:
        result = topic_filter(text)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        # Truncate long text for display
        display_text = text[:50] + "..." if len(text) > 50 else text
        action = "BLOCK" if result else "ALLOW"
        print(f"{status} | {action:5} | '{display_text}'")
    
    print("\n" + "=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print(f"Success Rate: {passed/len(test_cases)*100:.1f}%")
    print("=" * 70)
    
    # Statistics
    print("\n📊 FILTER STATISTICS:")
    print("-" * 70)
    print(f"Allowed topics: {len(ALLOWED_TOPICS)} keywords")
    print(f"Blocked topics: {len(BLOCKED_TOPICS)} keywords")
    print(f"Languages supported: English + Vietnamese")
    print("-" * 70)


# ============================================================
# EXPLANATION
# ============================================================

def explain_logic():
    """Explain the topic filter logic."""
    
    print("\n" + "=" * 70)
    print("HOW TOPIC FILTER WORKS")
    print("=" * 70)
    
    print("""
LOGIC FLOW:
1. Check for BLOCKED topics first (highest priority)
   → If found: BLOCK immediately (safety first)
   
2. Check for ALLOWED topics
   → If found: ALLOW (on-topic for banking)
   
3. If no allowed topic found
   → BLOCK (off-topic, not related to banking)

PRIORITY:
  BLOCKED topics > ALLOWED topics > Default (block)

EXAMPLES:
  ✅ "What is the savings rate?" 
     → Contains "savings" (allowed) → ALLOW
     
  ❌ "Recipe for chocolate cake"
     → No banking keywords → BLOCK (off-topic)
     
  ❌ "How to hack a bank account?"
     → Contains "hack" (blocked) → BLOCK (dangerous)
     → Even though it has "bank" and "account" (allowed)
     → Blocked topics take priority!

WHY THIS APPROACH?
  - Simple and fast (keyword matching)
  - Bilingual support (English + Vietnamese)
  - Safety first (blocked topics checked first)
  - Low false positives (specific banking keywords)
""")
    
    print("=" * 70)


# ============================================================
# ADVANCED: False Positive Analysis
# ============================================================

def analyze_false_positives():
    """Analyze potential false positives."""
    
    print("\n" + "=" * 70)
    print("FALSE POSITIVE ANALYSIS")
    print("=" * 70)
    
    edge_cases = [
        ("I want to transfer money", False, "Should ALLOW - clear banking intent"),
        ("transfer", False, "Should ALLOW - banking keyword"),
        ("I need help", True, "Should BLOCK - too generic, no banking context"),
        ("Hello", True, "Should BLOCK - greeting only, no banking intent"),
        ("Can you help me?", True, "Should BLOCK - generic question"),
        ("What can you do?", True, "Should BLOCK - meta question"),
    ]
    
    print("\nEdge Cases:")
    print("-" * 70)
    
    for text, expected, reason in edge_cases:
        result = topic_filter(text)
        status = "✅" if result == expected else "❌"
        action = "BLOCK" if result else "ALLOW"
        print(f"{status} {action:5} | '{text:30}' | {reason}")
    
    print("\n" + "=" * 70)
    print("TRADE-OFF:")
    print("  - Strict filtering = Low false negatives (good security)")
    print("  - Strict filtering = Higher false positives (may block valid queries)")
    print("  - Solution: Add more allowed keywords or use semantic matching")
    print("=" * 70)


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # Run tests
    run_tests()
    
    # Explain logic
    explain_logic()
    
    # Analyze false positives
    analyze_false_positives()
    
    print("\n✅ TODO 4 COMPLETED!")
    print("=" * 70)
