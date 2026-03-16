def caesar_encrypt(text: str, shift: int) -> str:
    """
    凯撒密码加密函数
    :param text: 明文文本
    :param shift: 偏移量（整数）
    :return: 加密后的密文
    """
    result = ""
    shift = shift % 26  # 确保偏移量在0-25之间，避免越界
    for char in text:
        if char.isupper():
            # 处理大写字母
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            # 处理小写字母
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # 非字母字符（数字、符号、空格等）直接保留
            result += char
    return result


def caesar_decrypt(text: str, shift: int) -> str:
    """
    凯撒密码解密函数
    :param text: 密文文本
    :param shift: 偏移量（需与加密时一致）
    :return: 解密后的明文
    """
    return caesar_encrypt(text, -shift)


def caesar_brute_force(ciphertext: str) -> list:
    """
    凯撒密码暴力破解函数（遍历所有偏移量）
    :param ciphertext: 待破解的密文
    :return: 包含所有偏移量及对应解密结果的列表
    """
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
    return results


if __name__ == "__main__":
    print("=== 凯撒密码加解密&暴力破解工具 ===")
    print("1. 加密")
    print("2. 解密")
    print("3. 暴力破解（无需偏移量）")
    choice = input("请选择功能（输入1/2/3）：")

    if choice == "1":
        plaintext = input("请输入需要加密的明文：")
        shift = int(input("请输入偏移量（整数）："))
        ciphertext = caesar_encrypt(plaintext, shift)
        print(f"\n加密结果：{ciphertext}")

    elif choice == "2":
        ciphertext = input("请输入需要解密的密文：")
        shift = int(input("请输入偏移量（整数）："))
        plaintext = caesar_decrypt(ciphertext, shift)
        print(f"\n解密结果：{plaintext}")

    elif choice == "3":
        ciphertext = input("请输入需要破解的密文：")
        results = caesar_brute_force(ciphertext)
        print("\n=== 暴力破解结果（遍历偏移量0-25）===")
        for shift, text in results:
            print(f"偏移量 {shift:2d}：{text}")
        print("\n提示：寻找语义通顺的结果即为正确解密内容")

    else:
        print("输入错误，请重新运行并选择1/2/3")