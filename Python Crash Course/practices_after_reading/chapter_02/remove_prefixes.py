# When working with strings, another common task is to remove a prefix. 
# Consider a URL with the common prefix https://. We want to remove this 
# prefix, so we can focus on just the part of the URL that users need to enter 
# into an address bar. Here’s how to do that:

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)

# When you see a URL in an address bar and the https:// part isn’t shown, 
# the browser is probably using a method like removeprefix() behind the 
# scenes.