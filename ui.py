import streamlit as st
import random as rd

class Main():
    def main(self):

        st.title("Password Generator")
        password_length = st.slider("Choose the length for your password",min_value=0,max_value=15)
        check_box_upper = st.checkbox("Add Upper case leeters")
        check_box_lower = st.checkbox("Add Lower case letters")
        check_box_special = st.checkbox("Add Special case letters")
        check_box_numbers  = st.checkbox("Add Numbers")

        def create_password():
            if st.button("Generate my password"):
                    selected_categories = []
                    if check_box_upper:
                        selected_categories.append('upper')
                    if check_box_lower:
                        selected_categories.append('lower')
                    if check_box_numbers:
                        selected_categories.append('numbers')
                    if check_box_special:
                        selected_categories.append('special')

                    if len(selected_categories) > password_length:
                        st.toast("Increase password length")
                    else:
                        upper_case = [chr(rd.randint(65, 90))]
                        lower_case = [chr(rd.randint(97, 122))]
                        special = [chr(rd.randint(35, 47))]
                        nums = [str(rd.randint(0, 9))]

                        password = []
                        if 'upper' in selected_categories:
                            password.append(rd.choice(upper_case))
                        if 'lower' in selected_categories:
                            password.append(rd.choice(lower_case))
                        if 'numbers' in selected_categories:
                            password.append(rd.choice(nums))
                        if 'special' in selected_categories:
                            password.append(rd.choice(special))

                        all_characters = []
                        if check_box_upper:
                            all_characters.extend([chr(i) for i in range(65, 91)])
                        if check_box_lower:
                            all_characters.extend([chr(i) for i in range(97, 123)])
                        if check_box_numbers:
                            all_characters.extend([str(i) for i in range(10)])
                        if check_box_special:
                            all_characters.extend([chr(i) for i in range(35, 48)])

                        while len(password) < password_length:
                            password.append(rd.choice(all_characters))

                        rd.shuffle(password)

                        return ''.join(password)
        st.text_area("Your password:",value=create_password())

m = Main()
m.main()
