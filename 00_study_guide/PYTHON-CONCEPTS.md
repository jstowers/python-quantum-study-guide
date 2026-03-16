# Python Concepts

## Assignment Copies a Reference, Not the Object Itself

You want to create two separate and distinct instances, `c1` and `c2`, of a `base_config` object, so you write:

```python
c1 = base_config
c2 = base_config
```

### Question

You append a string `x` to `c1.tags`.  Will `c2.tags` also have the `x` string?

```python
c1.tags.append("x")
```

### Answer

Yes, because `c1` and `c2` are not seperate instances.  They are two variable names pointing to the _same_ `base_config` object.  

In Python, assignment copies a reference, not the object itself.

```python
print(c1 is c2) # => true

assert c2.tags == [] # => false
```

To explicitly construct two distinct and independent instances, you must write something like:

```python
class Config:
    tags = []

c1 = Config()
c2 = Config()
c1.tags.append("x)
print(c2.tags)
```

## Formatted String Literals (`print(f)`)

The `f` marks the print statement as an `f-string` or formatted string literal.  This tells Python to evaluate any expression inside `{ }` and insert the result directly into the string.

```python
c1 = Config(frequency_hz=5.1e9, amplitude=0.5)
c2 = Config(frequency_hz=5.1e9, amplitude=0.5)

print(f'c1 == c2: {c1 == c2}')   # c1 == c2: True
print(f'c1 is c2: {c1 is c2}')   # c1 is c2: False
```

The expression `==` asks: _do these two objects have the same value?_

The expression `is` asks: _are these two objects the exact same object in memory?_


## Initial Commit

Sunday, March 15, 2026