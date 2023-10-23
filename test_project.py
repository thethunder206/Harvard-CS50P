import project

def test_add_account():
    project.add_account("John Doe", 1000, 20)
    assert project.balance("John Doe") == 1000

def test_remove_account():
    project.add_account("Jane Smith", 500, 21)
    project.remove_account("Jane Smith")
    assert project.balance("Jane Smith") == None

def test_deposit():
    project.add_account("Blink Doe", 1000, 30)
    project.deposit("Blink Doe", 500)
    assert project.balance("Blink Doe") == 1500

def test_withdraw():
    project.add_account("Abraham Doe", 1000, 45)
    project.withdraw("Abraham Doe", 500, 'CS50P')
    assert project.balance("Abraham Doe") == 500

def test_balance():
    project.add_account("Shiva Doe", 1000, 33)
    assert project.balance("Shiva Doe") == 1000

def test_all_info():
    project.clear()
    project.add_account("Bhim", 1000, 21)
    project.add_account("Jai", 500, 22)
    print(project.all_info())
    assert project.all_info() == [['Bhim', '1000', '21'], ['Jai', '500', '22']]